# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Adherent.conseil_local'
        db.delete_column('fcpe_adherent', 'conseil_local_id')


    def backwards(self, orm):
        
        # Adding field 'Adherent.conseil_local'
        db.add_column('fcpe_adherent', 'conseil_local', self.gf('django.db.models.fields.related.ForeignKey')(related_name='old', null=True, to=orm['fcpe.ConseilLocal']), keep_default=False)


    models = {
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
            'cfoyer': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11', 'blank': 'True'}),
            'clocal': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['communes.Commune']", 'null': 'True'}),
            'enfants': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'famille'", 'symmetrical': 'False', 'to': "orm['fcpe.Enfant']"}),
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
        'fcpe.engagement': {
            'Meta': {'object_name': 'Engagement'},
            'adherent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fcpe.Adherent']"}),
            'conseil_local': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fcpe.ConseilLocal']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fcpe.Role']"})
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
        'fcpe.role': {
            'Meta': {'object_name': 'Role'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libelle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['fcpe']
