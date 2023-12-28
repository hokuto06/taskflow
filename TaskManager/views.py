from django.utils import timezone
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db.models import Count
from .models import TasksList, SubTask
from .forms import CreateTaskForm
from datetime import datetime



def inicio(req):
    print(datetime.now())
    return render(req, 'base.html')

def dashboard(req):
    # Obtén las subtasks con estado = 3
    subtasks = SubTask.objects.filter(state=3)

    # Pasa las subtasks al contexto
    context = {'subtasks': subtasks}
    
    return render(req, 'dashboard.html', context)    

def task_list(req):
    return render(req, 'task_list.html')



# from datetime import timedelta

class TaskList(LoginRequiredMixin, ListView):
    model = TasksList
    template_name = "task_list.html"
    paginate_by = 6
    context_object_name = "prueba"

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = super().get_queryset().filter(owner=self.request.user)
        if query:
            queryset = queryset.filter(task_name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for task in context['prueba']:
            task.subtask_count = task.subtask_set.filter(open=True).count()

            total_subtasks = SubTask.objects.filter(sub_task_list=task).count()
            closed_subtasks = SubTask.objects.filter(sub_task_list=task, open=False).count()

            # total_subtasks = SubTask.objects.filter(task=task).count()
            # closed_subtasks = SubTask.objects.filter(task=task, open=False).count()
            # Evitar división por cero
            task.percentage_closed_subtasks = round((closed_subtasks / total_subtasks) * 100 if total_subtasks != 0 else 0)

            # Calcula el tiempo restante antes de que se cumpla el plazo
            if task.deadline:
                time_difference = task.deadline - timezone.now()
                task.time_difference = round(time_difference.total_seconds())
                task.time_difference_format = time_difference
        return context



class CreateTask(CreateView):
    
    model = TasksList
    template_name = "task_create_form.html"
    #fields = ["task_name","task_description","deadline","task_content"]
    success_url = "mylist"
   
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateTask, self).form_valid(form)

    def get_form_class(self):
        return CreateTaskForm

class TaskDetail(DetailView):

    model = TasksList
    template_name = "task_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.object
        rows = task.subtask_set.all()
        all_completed_rows = all(row.open for row in rows)
        context['all_completed_rows'] = all_completed_rows
        total_rows = rows.count()
        context['comentarios'] = rows
        context['total_rows'] = total_rows
        # task.subtask_count = task.subtask_set.filter(open=True).count()
        if task.deadline:
            # si hoy se cumple
            today = datetime.now().date()
            days_difference = (task.deadline.date() - today).days
            task.days_difference = days_difference
            print(days_difference)
            #             
            time_difference = task.deadline - timezone.now()
            task.time_difference = int(time_difference.total_seconds())
            task.time_difference_format = time_difference
        else:
            task.days_difference = None
        return context
    
class DeleteTask(DeleteView):
    model = TasksList
    template_name = "delete_task.html"
    success_url = "/task-flow/mylist"

# @require_POST
def create_subtask(request, task_id):
    subtask_name = request.POST.get('subTaskName')
    # Asegúrate de validar y procesar otros campos según tus necesidades
    print("subtask funcion")
    try:
        task = TasksList.objects.get(pk=task_id)
        SubTask.objects.create(sub_task=subtask_name, sub_task_list=task, open=True)
        return JsonResponse({'success': True, 'message': 'Subtask creada con éxito.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Error al crear Subtask: {str(e)}'})
    
def open_close_state(request, subtask_id, open_state):
    try:
        _subtask = SubTask.objects.get(pk=subtask_id)
        _subtask.open = open_state
        _subtask.save()
        return JsonResponse({'success': True})
    except SubTask.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Comentario no encontrado'})
    
def change_subtask_state(request, subtask_id, subtask_state):
    try:
        _subtask = SubTask.objects.get(pk=subtask_id)
        _subtask.state = subtask_state
        _subtask.save()
        return JsonResponse({'success': True})
    except SubTask.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Comentario no encontrado'})        