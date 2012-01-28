# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'RequestStore'
        db.create_table('core_requeststore', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('time', self.gf('django.db.models.fields.FloatField')()),
            ('query_coount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('core', ['RequestStore'])


    def backwards(self, orm):
        
        # Deleting model 'RequestStore'
        db.delete_table('core_requeststore')


    models = {
        'core.requeststore': {
            'Meta': {'object_name': 'RequestStore'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'query_coount': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.FloatField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']
