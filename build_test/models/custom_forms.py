from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import TabbedInterface, ObjectList, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.core import blocks

from wagtail_advanced_form_builder.models.abstract_advanced_email_form import AbstractAdvancedEmailForm
from wagtail_advanced_form_builder.models.abstract_advanced_form_field import AbstractAdvancedFormField
from wagtail_advanced_form_builder.blocks import InlineFormBlock

from modelcluster.fields import ParentalKey


class FormBuilderEmailFormField(AbstractAdvancedFormField):

    page = ParentalKey(
        'build_test.EmailFormBuilderPage',
        on_delete=models.CASCADE,
        related_name='form_fields'
    )


class EmailFormBuilderPage(AbstractAdvancedEmailForm):

    form_field = FormBuilderEmailFormField

    content = StreamField(
        [
            ('paragraph', blocks.RichTextBlock()),
            ('form', InlineFormBlock()),  # Provided by Wagtail Advanced Form Builder
        ],
        default=None,
        null=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=_('Content')),
        ObjectList(AbstractAdvancedEmailForm.content_panels, heading=_('Form')),
        ObjectList(Page.promote_panels, heading=_('Promote')),
        ObjectList(Page.settings_panels, heading=_('Settings'), classname="settings"),
    ])

    def get_template(self, request, *args, **kwargs):
        return 'build_test/email_form_builder_page.html'