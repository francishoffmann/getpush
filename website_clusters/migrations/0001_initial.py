# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WebsiteCluster'
        db.create_table('website_clusters_websitecluster', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('comment', self.gf('django.db.models.fields.CharField')(default='', max_length=400)),
        ))
        db.send_create_signal('website_clusters', ['WebsiteCluster'])

        # Adding model 'Website'
        db.create_table('website_clusters_website', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account_key', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('cluster', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website_clusters.WebsiteCluster'])),
            ('comment', self.gf('django.db.models.fields.CharField')(default='', max_length=400)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('return_url', self.gf('django.db.models.fields.CharField')(default='', max_length=400)),
            ('website_name', self.gf('django.db.models.fields.CharField')(default='', max_length=300)),
            ('website_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('website_clusters', ['Website'])

        # Adding model 'WebsiteIcon'
        db.create_table('website_clusters_websiteicon', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('website', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['website_clusters.Website'], unique=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=400)),
        ))
        db.send_create_signal('website_clusters', ['WebsiteIcon'])


    def backwards(self, orm):
        # Deleting model 'WebsiteCluster'
        db.delete_table('website_clusters_websitecluster')

        # Deleting model 'Website'
        db.delete_table('website_clusters_website')

        # Deleting model 'WebsiteIcon'
        db.delete_table('website_clusters_websiteicon')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'website_clusters.website': {
            'Meta': {'object_name': 'Website'},
            'account_key': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cluster': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website_clusters.WebsiteCluster']"}),
            'comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'return_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400'}),
            'website_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'}),
            'website_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'website_clusters.websitecluster': {
            'Meta': {'object_name': 'WebsiteCluster'},
            'comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'website_clusters.websiteicon': {
            'Meta': {'object_name': 'WebsiteIcon'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '400'}),
            'website': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website_clusters.Website']", 'unique': 'True'})
        }
    }

    complete_apps = ['website_clusters']