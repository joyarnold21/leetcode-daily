class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        day=[31,28,31,30,31,30,31,31,30,31,30,31]
        def somita(date):
            month,days= map(int,date.split("-"))
            return sum(day[:month-1])+days       
        start = max(somita(arriveAlice),somita(arriveBob))
        end= min(somita(leaveAlice),somita(leaveBob))
        return max(0,end-start+1)