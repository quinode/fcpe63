# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Article.section'
        db.delete_column('fcpe_article', 'section_id')

        # Adding field 'Article.category'
        db.add_column('fcpe_article', 'category', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='fcpe_article_rel', null=True, blank=True, to=orm['coop_cms.ArticleCategory']), keep_default=False)

        # Adding field 'Article.in_newsletter'
        db.add_column('fcpe_article', 'in_newsletter', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Adding field 'Article.is_homepage'
        db.add_column('fcpe_article', 'is_homepage', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Article.headline'
        db.add_column('fcpe_article', 'headline', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Changing field 'Article.title'
        db.alter_column('fcpe_article', 'title', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Article.content'
        db.alter_column('fcpe_article', 'content', self.gf('django.db.models.fields.TextField')())


    def backwards(self, orm):
        
        # Adding field 'Article.section'
        db.add_column('fcpe_article', 'section', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='fcpe_article_rel', null=True, to=orm['coop_cms.ArticleSection'], blank=True), keep_default=False)

        # Deleting field 'Article.category'
        db.delete_column('fcpe_article', 'category_id')

        # Deleting field 'Article.in_newsletter'
        db.delete_column('fcpe_article', 'in_newsletter')

        # Deleting field 'Article.is_homepage'
        db.delete_column('fcpe_article', 'is_homepage')

        # Deleting field 'Article.headline'
        db.delete_column('fcpe_article', 'headline')

        # Changing field 'Article.title'
        db.alter_column('fcpe_article', 'title', self.gf('html_field.db.models.fields.HTMLField')())

        # Changing field 'Article.content'
        db.alter_column('fcpe_article', 'content', self.gf('html_field.db.models.fields.HTMLField')())


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
        'coop_cms.articlecategory': {
            'Meta': {'object_name': 'ArticleCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'populate_from': "'name'", 'allow_duplicates': 'False', 'max_length': '100', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'overwrite': 'False', 'db_index': 'True'})
        },
        'django_mailman.list': {
            'Meta': {'object_name': 'List'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'encoding': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'fcpe.adherent': {
            'Meta': {'object_name': 'Adherent', '_ormbases': ['fcpe.Personne']},
            '_cl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            '_cp': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            '_ville': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'adhesion_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'adr1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'adr2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'annee_scolaire': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fcpe.AnneeScolaire']", 'null': 'True', 'blank': 'True'}),
            'cfoyer': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['communes.Commune']", 'null': 'True'}),
            'conseil_local': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['fcpe.ConseilLocal']", 'through': "orm['fcpe.Engagement']", 'symmetrical': 'False'}),
            'foyer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'rattachement'", 'null': 'True', 'to': "orm['fcpe.Foyer']"}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'personne_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fcpe.Personne']", 'unique': 'True', 'primary_key': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'fcpe.anneescolaire': {
            'Meta': {'object_name': 'AnneeScolaire'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libelle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'fcpe.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'fcpe_article_rel'", 'null': 'True', 'blank': 'True', 'to': "orm['coop_cms.ArticleCategory']"}),
            'content': ('django.db.models.fields.TextField', [], {'default': "u'Page content'", 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'headline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'publication': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'populate_from': "'title'", 'allow_duplicates': 'False', 'max_length': '100', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'overwrite': 'False', 'db_index': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'temp_logo': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'fcpe_article.html'", 'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'default': "u'Page title'", 'blank': 'True'})
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
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'primaire': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'secondaire': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'fcpe.enfant': {
            'Meta': {'object_name': 'Enfant'},
            'cfoyer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'famille'", 'to': "orm['fcpe.Foyer']"}),
            'classe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fcpe.Classe']"}),
            'etablissement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fcpe.Etablissement']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_classe_norma': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'fcpe.engagement': {
            'Meta': {'ordering': "['role']", 'object_name': 'Engagement'},
            'adherent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fcpe.Adherent']"}),
            'adhesion_primaire': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'conseil_local': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adhesions'", 'to': "orm['fcpe.ConseilLocal']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'default': "'8'", 'to': "orm['fcpe.Role']"})
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
            'adhesion_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'adr1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'adr2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'annee_scolaire': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fcpe.AnneeScolaire']", 'null': 'True', 'blank': 'True'}),
            'code_foyer': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['communes.Commune']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'fcpe.personne': {
            'Meta': {'object_name': 'Personne'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['django_mailman.List']", 'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'optout': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
