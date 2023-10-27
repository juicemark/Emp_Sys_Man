from django.shortcuts import render, redirect
from .models import Memo
from emp_app.forms import MemoForm


def memo_list(request):
    memos = Memo.objects.all()
    return render(request, 'memo/memo_list.html', {'memos': memos})


def memo_create(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('memo_list')
    else:
        form = MemoForm()
    return render(request, 'memo/memo_form.html', {'form': form})


def memo_update(request, pk):
    memo = Memo.objects.get(pk=pk)
    if request.method == 'POST':
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('memo_list')
    else:
        form = MemoForm(instance=memo)
    return render(request, 'memo/memo_form.html', {'form': form})


def memo_delete(request, pk):
    memo = Memo.objects.get(pk=pk)
    memo.delete()
    return redirect('memo_list')
