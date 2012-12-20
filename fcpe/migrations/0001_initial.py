# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ConseilLocal'
        db.create_table('fcpe_conseillocal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=9, blank=True)),
            ('adr1', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('adr2', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('commune', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['communes.Commune'])),
            ('_cp', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('_ville', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('fcpe', ['ConseilLocal'])

        # Adding model 'Etablissement'
        db.create_table('fcpe_etablissement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=8, blank=True)),
            ('adr1', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('adr2', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('commune', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['communes.Commune'], null=True)),
            ('perimetre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fcpe.ConseilLocal'])),
            ('_cp', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('_ville', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('fcpe', ['Etablissement'])

        # Adding model 'Classe'
        db.create_table('fcpe_classe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('libelle', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('fcpe', ['Classe'])

        # Adding model 'Personne'
        db.create_table('fcpe_personne', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('organisation', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('partenaire', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('fcpe', ['Personne'])

        # Adding model 'Enfant'
        db.create_table('fcpe_enfant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('etablissement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fcpe.Etablissement'])),
            ('classe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fcpe.Classe'])),
            ('id_classe_norma', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('fcpe', ['Enfant'])

        # Adding model 'Foyer'
        db.create_table('fcpe_foyer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=11, blank=True)),
        ))
        db.send_create_signal('fcpe', ['Foyer'])

        # Adding M2M table for field enfants on 'Foyer'
        db.create_table('fcpe_foyer_enfants', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('foyer', models.ForeignKey(orm['fcpe.foyer'], null=False)),
            ('enfant', models.ForeignKey(orm['fcpe.enfant'], null=False))
        ))
        db.create_unique('fcpe_foyer_enfants', ['foyer_id', 'enfant_id'])

        # Adding model 'Adherent'
        db.create_table('fcpe_adherent', (
            ('personne_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fcpe.Personne'], unique=True, primary_key=True)),
            ('foyer', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fcpe.Foyer'], unique=True, null=True)),
            ('conseil_local', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fcpe.ConseilLocal'], null=True)),
            ('adr1', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('adr2', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('commune', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['communes.Commune'])),
            ('adhesion_id', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True, blank=True)),
            ('annee_scolaire', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('au_bureau', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('fcpe', ['Adherent'])

        # Adding model 'Role'
        db.create_table('fcpe_role', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('libelle', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('fcpe', ['Role'])

        # Adding model 'Responsable'
        db.create_table('fcpe_responsable', (
            ('adherent_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fcpe.Adherent'], unique=True, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fcpe.Role'])),
        ))
        db.send_create_signal('fcpe', ['Responsable'])


    def backwards(self, orm):
        
        # Deleting model 'ConseilLocal'
        db.delete_table('fcpe_conseillocal')

        # Deleting model 'Etablissement'
        db.delete_table('fcpe_etablissement')

        # Deleting model 'Classe'
        db.delete_table('fcpe_classe')

        # Deleting model 'Personne'
        db.delete_table('fcpe_personne')

        # Deleting model 'Enfant'
        db.delete_table('fcpe_enfant')

        # Deleting model 'Foyer'
        db.delete_table('fcpe_foyer')

        # Removing M2M table for field enfants on 'Foyer'
        db.delete_table('fcpe_foyer_enfants')

        # Deleting model 'Adherent'
        db.delete_table('fcpe_adherent')

        # Deleting model 'Role'
        db.delete_table('fcpe_role')

        # Deleting model 'Responsable'
        db.delete_table('fcpe_responsable')


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
            'adhesion_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'adr1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'adr2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'annee_scolaire': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'au_bureau': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['communes.Commune']"}),
            'conseil_local': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fcpe.ConseilLocal']", 'null': 'True'}),
            'foyer': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fcpe.Foyer']", 'unique': 'True', 'null': 'True'}),
            'personne_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fcpe.Personne']", 'unique': 'True', 'primary_key': 'True'})
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
