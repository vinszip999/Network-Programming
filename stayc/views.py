from django.shortcuts import render

def show_j(request):
    context1 = {
        'name': '재이',
        'img_src': 'https://blogfiles.pstatic.net/MjAyMjAyMDhfNjQg/MDAxNjQ0MzI5OTUyOTE1.XXb7elmBsxSnpUWY38UIfSo7c2IWhfYa5IB01jwoBJcg.8MoiCCZxNtDn4PQ6XnHGHXkWzsOyI62G2BfTUVpINXMg.JPEG.guardened/FHwoZzzaMAkMfEw.jpg',
        # src 끝나는 부분에 , 컴마 넣어주기!! 언제 더 추가할지 모르니까 넣어주기!
    }
    return render(request, 'stayc/member.html', context=context1)


def show_yoon(request):
    context = {
        'name': '윤',
        'img_src': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA4MjJfMjcy%2FMDAxNjI5NjI3MjM0OTM2.DOvNqSm33SQ8xHrswOAiwAB7CLGKkdrs_jPjDQfJxTYg.-pMc0mII0QPDilH4eadWotB6j7dwWJsaV6KKnwD9qaMg.JPEG.niceguy00%2FSeul_%25BD%25BA%25C5%25D7%25C0%25CC%25BE%25BE_STEREOTYPE_22.jpg&type=sc960_832',
    }
    return render(request, 'stayc/member.html', context=context)
