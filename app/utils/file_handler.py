from fastapi import HTTPException, status

def validate_file(file):
    # Validate file type
    if file.content_type not in [
        "image/jpeg",
        "image/png",
        "image/webp",
        "application/pdf"
    ]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Upload JPG, PNG, WEBP, or PDF."
        )

    # Validate file size (max 10MB)
    file.file.seek(0, 2)  # Move to end of file
    size = file.file.tell()
    file.file.seek(0)     # Reset pointer

    if size > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File size exceeds 10MB."
        )
