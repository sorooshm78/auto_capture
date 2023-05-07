from asgiref.sync import async_to_sync
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from channels.layers import get_channel_layer

from .forms import CommandForm


class RunCommandView(LoginRequiredMixin, FormView):
    template_name = "command/index.html"
    success_url = reverse_lazy("command")
    form_class = CommandForm

    def form_valid(self, form):
        data = form.cleaned_data
        command = data.get("command")
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"client_{self.request.user.username}",
            {"type": "send_message", "command": command},
        )

        return super().form_valid(form)
