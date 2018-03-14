import json

from django.views import generic

class BaseView(generic.TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)

        initial_data = {}

        if self.request.user.id == None:
            user = None
        else:
            user = {
                'id': self.request.user.id,
                'username': self.request.user.username,
                'email': self.request.user.email,
                'is_superuser' : self.request.user.is_superuser,
                'is_staff' : self.request.user.is_staff,
            }

        initial_data['user'] = user

        context['initial_data'] = json.dumps(
            initial_data,
            ensure_ascii = False
        )

        return context
