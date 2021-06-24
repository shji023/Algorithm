from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    tmp_truck = deque([0] * bridge_length)
    timer = 0
    sum_truck = 0
    while tmp_truck:
        timer += 1
        sum_truck -= tmp_truck.popleft()

        if truck_weights:
            if sum_truck + truck_weights[0] <= weight:
                pop_truck = truck_weights.popleft()
                tmp_truck.append(pop_truck)
                sum_truck += pop_truck
            else:
                tmp_truck.append(0)
    return timer

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    while len(trucks_on_bridge):
        answer += 1
        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
    return answer