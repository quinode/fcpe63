# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AnneeScolaire'
        db.create_table('fcpe_anneescolaire', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('libelle', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('fcpe', ['AnneeScolaire'])

        # Renaming column for 'Adherent.annee_scolaire' to match new field type.
        db.rename_column('fcpe_adherent', 'annee_scolaire', 'annee_scolaire_id')
        # Changing field 'Adherent.annee_scolaire'
        db.alter_column('fcpe_adherent', 'annee_scolaire_id', self.gf('django.db.models.fields.related.ForeignKey')(default=6, to=orm['fcpe.AnneeScolaire']))

        # Adding index on 'Adherent', fields ['annee_scolaire']
        db.create_index('fcpe_adherent', ['annee_scolaire_id'])


    def backwards(self, orm):
        
        # Removing index on 'Adherent', fields ['annee_scolaire']
        db.delete_index('fcpe_adherent', ['annee_scolaire_id'])

        # Deleting model 'AnneeScolaire'
        db.delete_table('fcpe_anneescolaire')

        # Renaming column for 'Adherent.annee_scolaire' to match new field type.
        db.rename_column('fcpe_adherent', 'annee_scolaire_id', 'annee_scolaire')
        # Changing field 'Adherent.annee_scolaire'
        db.alter_column('fcpe_adherent', 'annee_scolaire', self.gf('django.db.models.fields.IntegerField')(null=True))


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
        'communes.commune': {
            'Meta': {'object_name': 'Commune'},
            'code_postal': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insee': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'maj': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'fcpe.adherent': {
            'Meta': {'object_name': 'Adherent', '_ormbases': ['fcpe.Personne']},
            '_cl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            '_cp': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            '_ville': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'adhesion_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'adr1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'adr2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'annee_scolaire': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fcpe.AnneeScolaire']"}),
            'au_bureau': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['communes.Commune']"}),
            'conseil_local': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fcpe.ConseilLocal']", 'null': 'True'}),
            'foyer': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fcpe.Foyer']", 'unique': 'True', 'null': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'personne_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fcpe.Personne']", 'unique': 'True', 'primary_key': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'fcpe.anneescolaire': {
            'Meta': {'object_name': 'AnneeScolaire'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libelle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'fcpe.classe': {
            'Meta': {'object_name': 'Classe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libelle': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'fcpe.conseillocal': {
            'Meta': {'object_name': 'ConseilLocal'},
            '_cp': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            '_ville': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'adr1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'adr2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '9', 'blank': 'True'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['communes.Commune']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'fcpe.enfant': {
            'Meta': {'object_name': 'Enfant'},
            'classe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fcpe.Classe']"}),
            'etablissement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fcpe.Etablissement']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_classe_norma': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'fcpe.etablissement': {
            'Meta': {'object_name': 'Etablissement'},
            '_cp': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            '_ville': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'adr1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'adr2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '8', 'blank': 'True'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['communes.Commune']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'perimetre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fcpe.ConseilLocal']"})
        },
        'fcpe.foyer': {
            'Meta': {'object_name': 'Foyer'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11', 'blank': 'True'}),
            'enfants': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['fcpe.Enfant']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'fcpe.personne': {
            'Meta': {'object_name': 'Personne'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'organisation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'partenaire': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'fcpe.responsable': {
            'Meta': {'object_name': 'Responsable', '_ormbases': ['fcpe.Adherent']},
            'adherent_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fcpe.Adherent']", 'unique': 'True', 'primary_key': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fcpe.Role']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'fcpe.role': {
            'Meta': {'object_name': 'Role'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libelle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['fcpe']
