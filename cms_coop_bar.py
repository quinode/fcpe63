from coop_cms.coop_bar_cfg import *


def admin_articles(request, context):
    if request and request.user.is_staff:
        return make_link(reverse('admin:fcpe_article_changelist'), 'Articles', 'fugue/documents-stack.png',
            classes=['icon', 'alert_on_click'])


def load_commands(coop_bar):
    coop_bar.register([

        [django_admin, admin_articles],  

        [cms_edit, cms_view, cms_save, cms_cancel, django_admin_edit_article, cms_article_settings],

        [cms_new_article, ],

        [cms_new_newsletter, edit_newsletter, cancel_edit_newsletter, save_newsletter,
            change_newsletter_settings,
            schedule_newsletter, test_newsletter],

        [cms_media_library, cms_upload_image, cms_upload_doc],

        [log_out]
    ])

