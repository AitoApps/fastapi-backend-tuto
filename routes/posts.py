
from fastapi import APIRouter, Depends, HTTPException, status
from dependencies import get_current_user
from models.posts import Post, PostType
from schema.posts import PostCreate
from schema.users import UserOut
from bson.objectid import ObjectId


router = APIRouter(prefix="/posts", tags=["post"])


@router.post("/test")
async def test(current_user=Depends(get_current_user)):

    return {"message": "Authenticated", "user_id": current_user}


@router.post("/")
async def create_post(post_data: PostCreate, current_user: UserOut = Depends(get_current_user)):
    print("RRR", current_user)
    match post_data.type:
        case PostType.post.value:
            post: Post = await Post(user_id=ObjectId(str(current_user.id)), text=post_data.text, type=post_data.type).insert()
            return post
        case PostType.repost.value:
            if not post_data.originalPostId or post_data.originalPostId == "":
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail="original post missing")
            post: Post = await Post(user_id=ObjectId(str(current_user.id)), text=post_data.text, type=post_data.type, originalPostId=post_data.originalPostId).insert()
            return post
        case PostType.reply.value:
            if not post_data.originalPostId or post_data.originalPostId == "":
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail="original post missing")
            post: Post = await Post(user_id=ObjectId(str(current_user.id)), text=post_data.text, type=post_data.type, originalPostId=post_data.originalPostId).insert()
            return post


@router.delete("/{post_id}")
async def delete_post(post_id: str, current_user: UserOut = Depends(get_current_user)):
    post: Post = await Post.get(post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post doesn't exist")
    await post.delete()
    return {"messaage": "post deleted successfullly"}


@router.get("/{post_id}")
async def get_post_by_id(post_id: str):
    post: Post = await Post.get(post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post doesn't exist")

    return post
