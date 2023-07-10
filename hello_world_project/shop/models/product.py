from django.db import models
from django.forms import FloatField
from django.utils import timezone 
from filer.fields import image
# from shop.money.fields import MoneyField 
# from djangocms_text_ckeditor.fields import HTMLField
from django.utils.translation import gettext_lazy as _


PRODUCT_CATEGORY = [
    ("Q&A", "Q&A"),
    ("Summarize for a 2nd grader", "Summarize for a 2nd grader"),
    ("Text to command", 'Text to command'),
    ("Keywords", "Keywords"),
    ("Code Generation", "Code Generation")
]

class Product(models.Model): 
        # common product fields
        name = models.CharField(
            max_length=255,
            verbose_name=_("Product Name"),
        )

        product_code = models.CharField(
            _("Product code"),
            max_length=255,
            unique=True,
        )
        
        category = models.CharField(choices=PRODUCT_CATEGORY,
                                max_length=300, default="Q&A")

        unit_price = FloatField( 
            help_text=_("Net price for this product"),
        )

        # controlling the catalog
        order = models.PositiveIntegerField(
            verbose_name=_("Sort by"),
            db_index=True,
        ) 
        
        show_breadcrumb = models.BooleanField(
            _("Show Breadcrumb"),
            default=True,
            help_text=_("Shall the detail page show the product's breadcrumb."),
        ) 
        
        sample_image = image.FilerImageField(
            verbose_name=_("Sample Image"),
            blank=True,
            null=True,
            default=None,
            on_delete=models.SET_DEFAULT,
            help_text=_("Sample image used in the catalog's list view."),
        )

        decription = models.TextField(
            verbose_name=_("decription"),
            blank=True,
            null=True,
            help_text=_("Short description for the catalog list view."),
        )

        created_at = models.DateTimeField(
        _("Created at"),auto_now_add=True,)

        updated_at = models.DateTimeField(
            _("Updated at"),
            auto_now=True,
        )

        active = models.BooleanField(
            _("Active"),
            default=True,
            help_text=_("Is this product publicly visible."),
        )