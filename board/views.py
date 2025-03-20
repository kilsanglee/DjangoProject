from django.shortcuts import render, redirect, get_object_or_404

from board.forms import BoardForm
from board.models import  Board
# Create your views here.
def board_list(request):
    print("===> board ")
    li = Board.objects.order_by('-id').all()
    context ={"li" : li }
    return render(request, 'board_list.html' ,context)

def board_form(request, ):
    if request.method !='POST':
        return  render(request, 'board_form.html')
    else:
        form = BoardForm(request.POST)
        form.save()
        '''
        title = request.POST.get('title')
        content = request.POST.get('content')
        board = Board(title=title, content=content)
        board.save()  # 데이터베이스에 저장
        '''
        return render(request, 'board_result.html')

def board_delete(request, pk):
    print("===> 삭제 ")
    board = get_object_or_404(Board, pk = pk)
    board.delete()
    return redirect('board_list')

def board_edit(request,pk):
    if request.method != 'POST':
        print("===> board ")
        board = get_object_or_404(Board, pk = pk)
        context ={"board" : board }
        return render(request, 'board_edit.html' ,context)
    else:
        print("===> Update (수정하기) ")
        board = get_object_or_404(Board, pk=pk)
        board = BoardForm(request.POST, instance=board)
        board.save()
        '''
        title = request.POST.get('title')
        content = request.POST.get('content')
        board.title = title
        board.content = content
        board.save()  # 데이터베이스에 수정하기
        '''
        return redirect('board_list')



