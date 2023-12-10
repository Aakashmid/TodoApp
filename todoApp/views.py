from django.shortcuts import render,redirect
from .models import Tasks
from datetime import datetime
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def home(request):
    tasks=Tasks.objects.all()
    context={'tasks':tasks}
    return render(request,'app\index.html',context)
def appendTask(request):
    if request.method=='POST':

        taskDesc=request.POST.get('tDesc')
        taskTime=request.POST.get('taskTime')
     
        DuplicateTask=Tasks.objects.filter(taskDesc=taskDesc,time=taskTime)
        if DuplicateTask:
            pass  
            # Do nothing
        else:
            task=Tasks(taskDesc=taskDesc,time=taskTime)
            task.save()
   
    
            messages.success(request,'Task is successfuly added !!')
        

    return redirect('/')
    # tasks=Tasks.objects.all()
    # context={'tasks':tasks}
    # return render(request,'app\index.html',context)

def deleteTask(request):
    try:
        if request.method=='GET':
            
            pk=request.GET.get('pk')
            task=Tasks.objects.get(sno=pk)
            task.delete()
            # task.is_active = False
            # task.save()
            response = JsonResponse({'message': 'data is deleted successfully'})
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            return response
 
        
    except Exception as e:
        print(e)
        return JsonResponse({'message': 'Internal Server Error'}, status=500)

def LoginHand(request):
    pass
def LogoutHand(request):
    pass