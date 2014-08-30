# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Member'
        db.create_table(u'members_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('susf_expiry', self.gf('django.db.models.fields.DateTimeField')()),
            ('club_expiry', self.gf('django.db.models.fields.DateTimeField')()),
            ('dob', self.gf('django.db.models.fields.DateTimeField')()),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('student', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'members', ['Member'])


    def backwards(self, orm):
        # Deleting model 'Member'
        db.delete_table(u'members_member')


    models = {
        u'members.member': {
            'Meta': {'object_name': 'Member'},
            'club_expiry': ('django.db.models.fields.DateTimeField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'dob': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'student': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'susf_expiry': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['members']