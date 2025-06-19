from import_export import resources, fields, widgets
from .models import Events, Country, StudyLevel

BASE_URL = "http://127.0.0.1:8000"  # or use domain from request in admin context

class EventsResource(resources.ModelResource):
    study_destination = fields.Field(
        column_name='study_destination',
        attribute='study_destination',
        widget=widgets.ManyToManyWidget(Country, field='country', separator=', ')
    )

    study_level = fields.Field(
        column_name='study_level',
        attribute='study_level',
        widget=widgets.ManyToManyWidget(StudyLevel, field='level_name', separator=', ')
    )

    def dehydrate_image(self, event):
        return f"{BASE_URL}{event.image.url}" if event.image else ""

    def dehydrate_card_image(self, event):
        return f"{BASE_URL}{event.card_image.url}" if event.card_image else ""

    class Meta:
        model = Events
        exclude = ['id', 'is_deleted', 'date_updated', 'slug']
