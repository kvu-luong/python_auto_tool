from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .forms import FriendForm
from .models import Friend

# Create your views here.

def indexView(request):
	form = FriendForm()
	friends = Friend.objects.all()
	return render(request, "index.html", {
		'form': form,
		'friends': friends
		})

def postFriend(request):
	#request should be ajax and method should be POST.
	if request.is_ajax and request.method == 'POST':
		form = FriendForm(request.POST)
		#save the data and after fetch the object in instance
		if form.is_valid():
			instance = form.save()
			ser_instance = serializers.serialize('json', [instance, ])
			#send to clint side
			return JsonResponse({'instance': ser_instance}, status=200)
		else:
			return JsonResponse({'error': form.errors}, status=400)	

	return JsonResponse({'error':''}, status=400)

def checkNickName(request):
	if request.is_ajax and request.method == 'GET':
		nick_name = request.GET.get('nick_name', None)
		if Friend.objects.filter(nick_name = nick_name).exists():
			return JsonResponse({"valid": False}, status = 200)
		else:
			return JsonResponse({"valid": True}, status = 200)

	return JsonResponse({}, status = 400)



from django.views import View

class FriendView(View):
    form_class = FriendForm
    template_name = "index.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        friends = Friend.objects.all()
        return render(self.request, self.template_name, 
            {"form": form, "friends": friends})

    def post(self, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST":
            form = self.form_class(self.request.POST)
            if form.is_valid():
                instance = form.save()
                ser_instance = serializers.serialize('json', [ instance, ])
                # send to client side.
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                return JsonResponse({"error": form.errors}, status=400)

        return JsonResponse({"error": ""}, status=400)
