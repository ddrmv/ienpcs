from django.core.exceptions import ValidationError


def web_image_size(instance):
    limit = 100 * 1024
    if instance.size > limit:
        raise ValidationError("Image file too large (>100 KB).")
