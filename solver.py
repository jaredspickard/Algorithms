# Put your solution here.
import networkx as nx
import random
# import queue as Q
import math

def solve(client):
    client.end()
    client.start()


    non_home = list(range(1, client.home)) + list(range(client.home + 1, client.v + 1))
    num_students = client.students
    num_bots = client.bots
    num_vertices = client.v
    num_edges = client.e
    scout_time = client.scout_time
    all_students = list(range(1, client.students + 1))


### --- TUTORIAL --- ###
    # client.scout(random.choice(non_home), all_students) # choose a random vertex to be scouted by every student

    # for _ in range(100):
    #     u, v = random.choice(list(client.G.edges())) # chooses two incident vertices randomly
    #     client.remote(u, v) # remotes along the edge

### ---------------------------------------------------------------------------------------- ###



# --- GREEDY SOLUTION, SCORE OF 85 --- #

    # for v in non_home:
    #     client.remote(v, client.home)

### ---------------------------------------------------------------------------------------- ###




# --- Send all scouts to every vertex, then remote from vertex to home in order of vertices that had the most reported bots: Score of 88 --- #
    # pq = PriorityQueue()
    # for v in non_home:
    #     r = client.scout(v, all_students)
    #     num_trues = sum([1 for i in r.values() if i])
    #     to_insert = (v, num_trues)
    #     pq.insert(to_insert)
    #
    # while (not pq.isEmpty()) and (client.bot_count[client.home] < 5):
    #     v = pq.delete()
    #     client.remote(v, client.home)

### ---------------------------------------------------------------------------------------- ###



# --- Same as above but we remote along shortest path with Dijkstra's, Score of ~90/1/3 --- #
#     pq = PriorityQueue()
#     djk = nx.single_source_dijkstra(client.G, client.home)
#     shortest_distances = djk[0]
#     shortest_paths = djk[1] # This is a dict {vertex:[path from home to vertex]} -> path is backwards
#
#     for v in non_home:
#         r = client.scout(v, all_students)
#         num_trues = sum([1 for i in r.values() if i])
#         to_insert = (v, num_trues)
#         pq.insert(to_insert)
#
#     while (not pq.isEmpty()) and (client.bot_count[client.home] < 5):
#         v = pq.delete()
#         short_path = shortest_paths[v]
#         short_path.reverse()
#         for i in range(len(short_path) - 1):
#             client.remote(short_path[i], short_path[i+1])


### ---------------------------------------------------------------------------------------- ###


# --- New Probability's and weights --- #

    # student_to_lies = {} # student_to_lies[i]=k means student i has lied k times
    # vertices_to_predictions = {} # vertices_to_predictions[v] = {i:L} means vertex v had student i report L
    # vertices_to_weights = {}
    # pq = PriorityQueue()
    # djk = nx.single_source_dijkstra(client.G, client.home)
    # shortest_distances = djk[0]
    # shortest_paths = djk[1]  # This is a dict {vertex:[path from home to vertex]} -> path is backwards
    # non_checked = non_home.copy()
    #
    # # reverse all the paths so that that they are vertex -> home
    # for _, path in shortest_paths.items():
    #     path.reverse()
    #
    #
    # def multiplier(num_lies):
    #     """Returns a multiplier for calculating weights based on # of lies"""
    #     return 0.0051 * num_lies + 0.745
    #
    # def update_vertices_student(student):
    #     """Updates all vertices_to_weights by student"""
    #     for v in non_checked:
    #         curr_label = vertices_to_predictions[v][student]
    #         vertices_to_weights[v] -= curr_label * multiplier(student_to_lies[student])
    #         student_to_lies[student] += 1
    #         vertices_to_weights[v] += curr_label * multiplier(student_to_lies[student])
    #
    #
    # def update_pq():
    #     """Constrcuts and returns a new PQ by vertices_to_weights"""
    #     new_pq = PriorityQueue()
    #     for v, w in vertices_to_weights.items():
    #         if v in non_checked:
    #             new_pq.insert((v, w))
    #     return new_pq
    #
    #
    #
    # # init all students to no lies
    # for student in all_students:
    #     student_to_lies[student] = 0
    #
    #
    # # First scout EVERY vertex w/ ALL students and init the vertices weights and construct pq
    # for v in non_home:
    #     student_to_label = client.scout(v, all_students)
    #     new_student_to_labels = {}
    #     w = 0
    #     for stud, predic in student_to_label.items():
    #         if predic:
    #             new_student_to_labels[stud] = 1
    #         else:
    #             new_student_to_labels[stud] = -1
    #         w += new_student_to_labels[stud] * multiplier(student_to_lies[stud])
    #     vertices_to_predictions[v] = new_student_to_labels
    #     vertices_to_weights[v] = w
    #     pq.insert((v, w))
    #
    #
    # # Now we call remote from the PQ and update vertices weights continuously if they lie
    # while (client.bot_count[client.home] < 5) and (not pq.isEmpty()):
    #
    #     v = pq.delete()
    #     short_path = shortest_paths[v] # gives shortest path from v -> home
    #
    #     for i in range(len(short_path) - 1):
    #         curr_vert = short_path[i]
    #         next_vert = short_path[i+1]
    #         num_remoted = client.remote(curr_vert, next_vert)
    #         if curr_vert in non_checked:
    #             non_checked.remove(curr_vert)
    #         # now lets see who lied
    #         if num_remoted == 0:
    #             correct_label = -1
    #         else:
    #             correct_label = 1
    #         predictions = vertices_to_predictions[curr_vert]
    #         for student, label in predictions.items():
    #             if label != correct_label:
    #                 update_vertices_student(student)
    #         if num_remoted == 0: # if our guess was wrong, stop and move to the next vertex
    #             break
    #
    #     # now re-update the PQ
    #     pq = update_pq()

### --------------------------------------------------------------------------- ###


### --- Adding a new way to go home BROKEN --- ###

    # student_to_lies = {} # student_to_lies[i]=k means student i has lied k times
    # vertices_to_predictions = {} # vertices_to_predictions[v] = {i:L} means vertex v had student i report L
    # vertices_to_weights = {} # Weights for each vertex for PQ
    # pq = PriorityQueue()
    # djk = nx.single_source_dijkstra(client.G, client.home)
    # shortest_distances = djk[0] # Dict {vertex:dist to home}
    # shortest_paths = djk[1]  # This is a dict {vertex:[path from home to vertex]} -> path is backwards
    # non_checked = non_home.copy() # available remote spaces
    # bots = [] # a list of known bot locations
    # to_scout  = all_students[:]
    #
    #
    # def multiplier(num_lies):
    #     """Returns a multiplier for calculating weights based on # of lies"""
    #     return 0.0051 * num_lies + 0.745
    #     # return 0.01 * num_lies + 0.745
    #     # return 0.147*math.log(num_lies + 1) + 0.75
    #
    # def weird_func(t, f):
    #     return (0.75 ** t * 0.25 ** f / 20) / ((0.75 ** t * 0.25 ** f / 20) + (0.75 ** f * 0.25 ** t * 19 / 20))
    #
    #
    # def update_vertices_student(student):
    #     """For a student who lied, remove their old weights from vertices and add a new weight"""
    #     for v in non_checked:
    #         predics = vertices_to_predictions[v]
    #         num_true = sum([1 for i in predics if i==1])
    #         num_false = sum([1 for i in predics if i==-1])
    #         curr_label = vertices_to_predictions[v][student]
    #         vertices_to_weights[v] -= curr_label * multiplier(student_to_lies[student])
    #         # vertices_to_weights[v] -= idk(num_true, num_false, student_to_lies[student], len(non_checked), 5 - len(bots))
    #         student_to_lies[student] += 1
    #         vertices_to_weights[v] += curr_label * multiplier(student_to_lies[student])
    #         # vertices_to_weights[v] += idk(num_true, num_false, student_to_lies[student], len(non_checked), 5 - len(bots))
    #
    #
    # def update_pq():
    #     """Constrcuts and returns a new PQ by vertices_to_weights"""
    #     new_pq = PriorityQueue()
    #     for v, w in vertices_to_weights.items():
    #         if v in non_checked:
    #             new_pq.insert((v, w))
    #     return new_pq
    #
    # ################
    # # Init Methods #
    # ################
    #
    # # reverse all the paths from home so that that they are vertex -> home
    # for _, path in shortest_paths.items():
    #     path.reverse()
    #
    # # init all students to no lies
    # for student in all_students:
    #     student_to_lies[student] = 0
    #
    # # First scout EVERY vertex w/ ALL students, init the vertices weights, construct pq
    # for v in non_home:
    #     student_to_label = client.scout(v, to_scout)
    #     new_student_to_labels = {}
    #     w = 0
    #     num_true = sum([1 for i in student_to_label.values() if i])
    #     num_false = sum([1 for i in student_to_label.values() if not i])
    #     for stud, predic in student_to_label.items():
    #         if predic:
    #             new_student_to_labels[stud] = 1
    #         else:
    #             new_student_to_labels[stud] = -1
    #         w += new_student_to_labels[stud] * multiplier(student_to_lies[stud])
    #         # w += idk(num_true, num_false, student_to_lies[stud], len(non_checked), 5 - len(bots))
    #     vertices_to_predictions[v] = new_student_to_labels
    #     vertices_to_weights[v] = w
    #     pq.insert((v, w))
    #
    # ########################
    # # Find bot's locations #
    # ########################
    #
    # # Now we call remote from the PQ and update vertices weights continuously if they lie
    # while (len(bots) < 5) and (not pq.isEmpty()):
    #     v = pq.delete()
    #     short_path = shortest_paths[v] # gives shortest path from v -> home
    #     num_remoted = client.remote(v, short_path[1]) # remote v -> next vertex from dijkstras
    #     if v in non_checked:
    #         non_checked.remove(v)  # remove from list of vertices to remote
    #     if num_remoted == 0:
    #         correct_label = -1
    #     else:
    #         # if we remoted bots, now we know their exact locations
    #         correct_label = 1
    #         # okay add to list of known bots
    #         for _ in range(num_remoted):
    #             bots.append(short_path[1])
    #         # also if we appended the new vertex delete an old one so no double counting
    #         old_bots = bots.copy()
    #         for loc in old_bots: # if we remoted bots we already knew about remove their old locations from bots
    #             if loc == v:
    #                 bots.remove(loc)
    #     # check who lied
    #     predictions = vertices_to_predictions[v]
    #     for student, label in predictions.items():
    #         if label != correct_label:
    #             # update vertex_to_weights for each student
    #             update_vertices_student(student)
    #     # set pq to vertex_to_weights
    #     pq = update_pq()
    #
    # #################################
    # # Bots found, remote them home #
    # #################################
    # print("Bots found")
    # # filter bots in some are already home
    # bots = [b for b in bots if b!=client.home]
    # # sort bots by ascending distance from home
    # bots_copy = bots.copy()
    # bots_sorted = []
    # while len(bots_copy) > 0:
    #     m = float("inf")
    #     item = 0
    #     for b in bots_copy:
    #         if shortest_distances[b] < m:
    #             m = shortest_distances[b]
    #             item = b
    #     bots_sorted.append(item)
    #     bots_copy.remove(item)
    #
    #
    #
    # bots = bots_sorted
    # verts_to_remote = []
    # final_paths = {}
    # for i, bot_location in enumerate(bots):
    #     if i==0: # for closest bot to home, its path will be to home
    #         verts_to_remote += shortest_paths[bot_location]
    #         final_paths[bot_location] = shortest_paths[bot_location]
    #     else:
    #         if bot_location in final_paths.keys():
    #             # if we already have a path for this bot, skip
    #             continue
    #         new_djk = nx.single_source_dijkstra(client.G, bot_location)
    #         new_shortest_distances = new_djk[0]
    #         new_shortest_paths = new_djk[1]
    #         x = {}
    #         for v in verts_to_remote: # check if dist to any of these points is shorter than to home
    #             if new_shortest_distances[v] <= shortest_distances[bot_location]:
    #                 x[v] = new_shortest_distances[v]
    #         if len(x) > 0:
    #             min_dist = float("inf")
    #             to_go = client.home
    #             for key, val in x.items():
    #                 if val < min_dist:
    #                     min_dist = val
    #                     to_go = key
    #             final_paths[bot_location] = new_shortest_paths[to_go]
    #             verts_to_remote += new_shortest_paths[to_go]
    #         else:
    #             # if it is not quicker to send the bot to another bots path, its path will be to home
    #             final_paths[bot_location] = shortest_paths[bot_location]
    #             verts_to_remote += shortest_paths[bot_location]
    #
    #
    # # now send bots on their path
    # verts_remoted = []
    # bots.reverse() # now it is in descending order (opposite of prev loop)
    # for bot in bots:
    #     cur_path = final_paths[bot]
    #     for i in range(len(cur_path) - 1):
    #         if cur_path[i] not in verts_remoted:
    #             client.remote(cur_path[i], cur_path[i+1])
    #         verts_remoted.append(cur_path[i])




### --------------------------------------------------------------------------- ###


### --- Same as above but moving along smallest edge to find instead of dijkstra edge --- ###

    student_to_lies = {} # student_to_lies[i]=k means student i has lied k times
    vertices_to_predictions = {} # vertices_to_predictions[v] = {i:L} means vertex v had student i report L
    vertices_to_weights = {} # Weights for each vertex for PQ
    pq = PriorityQueue()
    djk = nx.single_source_dijkstra(client.G, client.home)
    shortest_distances = djk[0] # Dict {vertex:dist to home}
    shortest_paths = djk[1]  # This is a dict {vertex:[path from home to vertex]} -> path is backwards
    non_checked = non_home.copy() # available remote spaces
    bots = [] # a list of known bot locations
    to_scout  = all_students[:]


    def multiplier(num_lies):
        """Returns a multiplier for calculating weights based on # of lies"""
        # return 0.0051 * num_lies + 0.745 # update with max multiplier at 50 lies
        return min([0.01 * num_lies + 0.745, 1]) # update with max multiplier at 25 lies
        # return 0.147*math.log(num_lies + 1) + 0.75 # logarithmic update


    def update_vertices_student(student):
        """For a student who lied, remove their old weights from vertices and add a new weight"""
        for v in non_checked:
            curr_label = vertices_to_predictions[v][student]
            vertices_to_weights[v] -= curr_label * multiplier(student_to_lies[student])
            student_to_lies[student] += 1
            vertices_to_weights[v] += curr_label * multiplier(student_to_lies[student])


    def update_pq():
        """Constrcuts and returns a new PQ by vertices_to_weights"""
        new_pq = PriorityQueue()
        for v, w in vertices_to_weights.items():
            if v in non_checked:
                new_pq.insert((v, w))
        return new_pq

    ################
    # Init Methods #
    ################

    # reverse all the paths from home so that that they are vertex -> home
    for _, path in shortest_paths.items():
        path.reverse()

    # init all students to no lies
    for student in all_students:
        student_to_lies[student] = 0

    # First scout EVERY vertex w/ ALL students, init the vertices weights, construct pq
    for v in non_home:
        student_to_label = client.scout(v, to_scout)
        new_student_to_labels = {}
        w = 0
        for stud, predic in student_to_label.items():
            if predic:
                new_student_to_labels[stud] = 1
            else:
                new_student_to_labels[stud] = -1
            w += new_student_to_labels[stud] * multiplier(student_to_lies[stud])
        vertices_to_predictions[v] = new_student_to_labels
        vertices_to_weights[v] = w
        pq.insert((v, w))

    ########################
    # Find bot's locations #
    ########################

    # Now we get vertex from PQ and call remote to nearest vertex, update vertices weights continuously if they lie
    while (len(bots) < 5) and (not pq.isEmpty()):
        v = pq.delete()
        # find nearest vertex to v
        min_weight = float("inf")
        vertex_to_take = 0
        for edge in client.G.edges(v):
            weight = client.G[edge[0]][edge[1]]['weight']
            if weight < min_weight:
                min_weight = weight
                vertex_to_take = edge[1]
        num_remoted = client.remote(v, vertex_to_take) # remote v -> next closest vertex
        if v in non_checked:
            non_checked.remove(v)  # remove from list of vertices to remote
        if num_remoted == 0:
            correct_label = -1
        else:
            # if we remoted bots, now we know their exact locations
            correct_label = 1
            # Add to list of known bots
            for _ in range(num_remoted):
                bots.append(vertex_to_take)
            # If we remoted a bot we were already counting, delete its old position from bots
            old_bots = bots.copy()
            for loc in old_bots: # if we remoted bots we already knew about remove their old locations from bots
                if loc == v:
                    bots.remove(loc)
        # check who lied and update other vertices
        predictions = vertices_to_predictions[v]
        for student, label in predictions.items():
            if label != correct_label:
                # update vertex_to_weights for each student
                update_vertices_student(student)
        # set pq to vertex_to_weights
        pq = update_pq()


    #################################
    # Bots found, remote them home #
    #################################


    print("Bots found")
    # remove bots who are already home
    bots = [b for b in bots if b!=client.home]
    # sort bots by increasing distance from home
    bots_copy = bots.copy()
    bots_sorted = []
    while len(bots_copy) > 0:
        m = float("inf")
        item = 0
        for b in bots_copy:
            if shortest_distances[b] < m:
                m = shortest_distances[b]
                item = b
        bots_sorted.append(item)
        bots_copy.remove(item)

    # Find the best path for each vertex to get home
    # Closest vertex to home's path will be straight to home
    # Other vertices can either go home or go to any vertex that will already be remoted if it is quicker
    bots = bots_sorted
    verts_to_remote = []
    final_paths = {} # paths we must remote
    for i, bot_location in enumerate(bots):
        if i==0: # for closest bot to home, its path will be to home
            verts_to_remote += shortest_paths[bot_location]
            final_paths[bot_location] = shortest_paths[bot_location]
        else:
            # if we already have a path for this bot, skip
            if bot_location in final_paths.keys():
                continue
            # Run Dijkstra's from bot_location to all other vertices
            new_djk = nx.single_source_dijkstra(client.G, bot_location)
            new_shortest_distances = new_djk[0]
            new_shortest_paths = new_djk[1]
            # Out of vertices that will be remoted, find those that are closer than home to bot_location
            x = {}
            for v in verts_to_remote: # check if dist to any of these points is shorter than to home
                if new_shortest_distances[v] <= shortest_distances[bot_location]:
                    x[v] = new_shortest_distances[v]
            if len(x) > 0:
                # Out of these vertices, find the closest
                min_dist = float("inf")
                to_go = client.home
                for key, val in x.items():
                    if val < min_dist:
                        min_dist = val
                        to_go = key
                final_paths[bot_location] = new_shortest_paths[to_go]
                verts_to_remote += new_shortest_paths[to_go]
            else:
                # if it is not quicker to send the bot to another bots path, its path will be to home
                final_paths[bot_location] = shortest_paths[bot_location]
                verts_to_remote += shortest_paths[bot_location]


    # now send bots on their path in order of farthest distance from home to closest
    verts_remoted = []
    bots.reverse()
    for bot in bots:
        cur_path = final_paths[bot]
        for i in range(len(cur_path) - 1):
            if cur_path[i] not in verts_remoted:
                client.remote(cur_path[i], cur_path[i+1])
            verts_remoted.append(cur_path[i])









    client.end()


    pass

# Priority queue was gotten from GeeksforGeeks https://www.geeksforgeeks.org/priority-queue-in-python/
# Modified for our purposes
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

        # for checking if the queue is empty

    def isEmpty(self):
        return len(self.queue) == []

        # for inserting an element in the queue, A TUPLE OF FORM (KEY, COUNT)

    def insert(self, data):
        self.queue.append(data)

        # for popping an element based on Priority

    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i][1] > self.queue[max][1]:
                    max = i
            item = self.queue[max][0]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()


