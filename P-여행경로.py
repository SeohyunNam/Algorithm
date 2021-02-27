# 2021-02-27
# src : https://gurumee92.tistory.com/165
def solution(tickets):
    # 1. �׷��� ����
    routes = dict()

    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]  
    # 2. ������ - [����] �������� ����    
    for r in routes.keys():
        routes[r].sort(reverse=True)

    # 3. DFS �˰������� path�� �������.
    st = ["ICN"]
    path = []
    
    while st:
        top = st[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(st.pop())
        else:
            st.append(routes[top].pop())
    
    # 4. ���� path�� �Ųٷ� ����.
    answer = path[::-1]
    return answer