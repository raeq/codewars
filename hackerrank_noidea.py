def do_work(p_array, p_like, p_dislike):
    p_like = p_like - p_dislike
    p_dislike = p_dislike - p_like

    positives = sum(1 for x in p_array if x in p_like)
    negatives = sum(-1 for x in p_array if x in p_dislike)

    return positives + negatives

    ...


if __name__ == '__main__2':
    meta = input().strip().split()
    array = input().strip().split()
    like = set(input().strip().split())
    dislike = set(input().strip().split())

    print(do_work(array, like, dislike))

if __name__ == '__main__':
    array = ['1', '5', '3']
    like = {'1', '3'}
    dislike = {'7', '5'}

    print(array, like, dislike)
    print(do_work(array, like, dislike))
