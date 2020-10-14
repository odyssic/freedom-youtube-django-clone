def validate_file_extension(value):

    import os
    from django.core.exceptions import ValidationError

    ext = os.path.splitext(value)[1]  # [0] returns path+filename
    valid_extensions = ['.heic', '.heif', '.webp', '.png', '.jpg', '.svg', '.pdf,', '.gif', '.ai', '.fig', '.sketch']

# if not valid: 

    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')