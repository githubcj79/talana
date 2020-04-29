from django.shortcuts import render

# Create your views here.

from .models import Car, CarInstance


def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_cars = Car.objects.all().count()
    num_instances = CarInstance.objects.all().count()
    # Available instances of cars
    num_instances_available = CarInstance.objects.filter(status__exact='a').count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_cars': num_cars, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available,
                 'num_visits': num_visits},
    )


from django.views import generic


class CarListView(generic.ListView):
    """Generic class-based view for a list of cars."""
    model = Car
    paginate_by = 10


class CarDetailView(generic.DetailView):
    """Generic class-based detail view for a car."""
    model = Car

