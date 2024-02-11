from django.core.exceptions import ValidationError


def web_image_size(instance):
    """Validator for user-uploaded Pc image file size."""
    limit = 100 * 1024
    if instance.size > limit:
        raise ValidationError("Image file too large (>100 KB).")
