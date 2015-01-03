from __future__ import unicode_literals
from mogwai.migrations.migrators import SchemaMigration


class Migration(SchemaMigration):

    # depends on this any other migration files?
    depends_on = (
        # FUTURE: ("otherapp", "0001_initial"),
        # CURRENT:
        '0001_initial'
    )

    def forwards(self, db):
        # Adding property 'phone' to 'Person'
        db.add_property(
            'person', 'person_phone',
            self.gf('mogwai.properties.String')(required=False, max_length=15, default=None),
            keep_default=False,
        )

    def backwards(self, db):

        # Delete property 'phone' from 'Person'
        db.delete_property(
            'person', 'person_phone'
        )

    models = {
        'models.Trinket': {
            'type': 'vertex',
            'label': 'trinket',
            'name': ('mogwai.properties.String', {'required': 'True', 'max_length': '1024'})
        },
        'models.Person': {
            'type': 'vertex',
            'label': 'person',
            'name': ('mogwai.properties.String', {'required': 'True', 'max_length': '512'}),
            'email': ('mogwai.properties.Email', {'required': 'True'}),
            'phone': ('mogwai.properties.String', {'required': 'False', 'max_length': '15'})
        },
        'models.OwnsObject': {
            'type': 'edge',
            'label': 'owns',
            'since': ('mogwai.properties.DateTime', {'required': 'True'})
        }
    }

