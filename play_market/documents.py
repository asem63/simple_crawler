from django_elasticsearch_dsl import DocType, Index, fields
from .models import Category, App

category = Index('category')
# See Elasticsearch Indices API reference for available settings
category.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@category.doc_type
class CategoryDocument(DocType):
    class Meta:
        model = Category  # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'mnemonic_name',
            'title'
        ]
        related_models = [App]


app = Index('app')
# See Elasticsearch Indices API reference for available settings
app.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@app.doc_type
class AppDocument(DocType):
    category = fields.ObjectField(properties={
        'mnemonic_name': fields.TextField(),
        'title': fields.TextField(),
    })

    class Meta:
        model = App  # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'app_id',
            'title',
            'image',
            'description',
            'url',
            'dev',
            'dev_id',
            'score',
        ]
        related_models = [Category]
