# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(friends)
        visited = [False] * n
        queue = deque([id])
        visited[id] = True
        current_level = 0

        while queue and current_level < level:
            for _ in range(len(queue)):
                person = queue.popleft()
                for f in friends[person]:
                    if not visited[f]:
                        visited[f] = True
                        queue.append(f)
            current_level += 1

        video_count = Counter()
        for friend_id in queue:
            for video in watchedVideos[friend_id]:
                video_count[video] += 1

        result = sorted(video_count.keys(), key=lambda x: (video_count[x], x))
        return result
