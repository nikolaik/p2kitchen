from django.http import HttpResponseBadRequest, HttpResponse
from django.views import View

from p2coffee.forms import SensorEventForm
from p2coffee.models import Machine
from p2coffee.sensor_events import handle_event_created


class CreateSensorEventView(View):
    """
    Logs a sensor event and runs on_new_meter task

    EXAMPLE request:
        GET /event/log/?name=power-meter-has-changed&id=ZWayVDev_zway_2-0-49-4&value=4.6
    """

    def get(self, request, *args, **kwargs):
        form = SensorEventForm(request.GET)

        if not form.is_valid():
            return HttpResponseBadRequest("Curse you coffeepot!")

        event = form.save(commit=False)
        machine, created = Machine.objects.get_or_create(device_name=event.id, defaults={"name": event.id})
        event.machine = machine
        event.save()

        handle_event_created(event)

        return HttpResponse("Thank you coffepot!")
