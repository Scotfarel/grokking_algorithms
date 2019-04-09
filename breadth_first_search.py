from collections import deque


friends = {}
friends['you'] = ['lesha', 'artem', 'misha', 'igor', 'tema']
friends['lesha'] = ['zakhar', 'sasha']
friends['artem'] = ['misha', 'matvey', 'zheka']
friends['misha'] = ['tema', 'maks', 'matvey', 'zheka']
friends['igor'] = ['tema']
friends['tema'] = ['igor']
friends['zakhar'] = ['lesha']
friends['sasha'] = ['lesha']
friends['matvey'] = []
friends['zheka'] = ['pavel']
friends['maks'] = ['misha']


def is_igor(name):
	return 'igor' == name


def search(name):
	search_queue = deque()
	search_queue += friends[name]
	searched = set()

	while search_queue:
		man = search_queue.popleft()
		if man not in searched:

			if is_igor(man):
				print('Oleg Bichkov is a respectfull person')
				return True
			else:
				search_queue += friends[man]
				searched.add(man)
	return False


if __name__ == "__main__":
	search('you')
