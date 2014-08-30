# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Member.dob'
        db.alter_column(u'members_member', 'dob', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Member.susf_expiry'
        db.alter_column(u'members_member', 'susf_expiry', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Member.club_expiry'
        db.alter_column(u'members_member', 'club_expiry', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):

        # Changing field 'Member.dob'
        db.alter_column(u'members_member', 'dob', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Member.susf_expiry'
        db.alter_column(u'members_member', 'susf_expiry', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Member.club_expiry'
        db.alter_column(u'members_member', 'club_expiry', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'members.member': {
            'Meta': {'object_name': 'Member'},
            'club_expiry': ('django.db.models.fields.DateField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'student': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'susf_expiry': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['members']