class LogServer:
    def __init__(self, max_logs):
        self.max_logs = max_logs
        self.logs = []

    def recordLog(self, logId, timestamp):
        self.logs.append((logId, timestamp))
        self.logs.sort(key=lambda x: x[1])

    def getLogs(self):
        if not self.logs:
            return ''
        
        current_time = self.logs[-1][1]
        hour_ago = current_time - 3600
        
        recent_logs = []
        for logId, timestamp in self.logs:
            if timestamp > hour_ago:
                recent_logs.append(str(logId))
        
        if len(recent_logs) > self.max_logs:
            recent_logs = recent_logs[-self.max_logs:]
            
        return ','.join(recent_logs)

    def getLogCount(self):
        if not self.logs:
            return 0
            
        current_time = self.logs[-1][1]
        hour_ago = current_time - 3600
        
        count = 0
        for _, timestamp in self.logs:
            if timestamp > hour_ago:
                count += 1
                
        return count

def run_test_case(max_logs, queries):
    print(f"\nRunning test with max_logs={max_logs}")
    log_server = LogServer(max_logs)
    
    for query in queries:
        query = query.split()
        query_type = query[0]
        
        if query_type == "RECORD":
            log_server.recordLog(int(query[1]), int(query[2]))
            print(f"Recording log: ID={query[1]}, timestamp={query[2]}")
        elif query_type == "GET_LOGS":
            result = log_server.getLogs()
            print(f"GET_LOGS: {result}")
        elif query_type == "COUNT":
            count = log_server.getLogCount()
            print(f"COUNT: {count}")
    print()

if __name__ == '__main__':
    # Sample Case 0
    print("=== Sample Case 0 ===")
    max_logs = 100
    queries = [
        "RECORD 1 0",
        "RECORD 2 300",
        "GET_LOGS",
        "COUNT",
        "RECORD 3 1200",
        "RECORD 1 1800",
        "GET_LOGS",
        "COUNT",
        "RECORD 4 3900",
        "GET_LOGS"
    ]
    run_test_case(max_logs, queries)

    # Sample Case 1
    print("=== Sample Case 1 ===")
    max_logs = 2
    queries = [
        "RECORD 1 0",
        "RECORD 7 600",
        "RECORD 3 1200",
        "RECORD 5 1800",
        "GET_LOGS",
        "COUNT",
        "RECORD 2 2400",
        "GET_LOGS",
        "COUNT"
    ]
    run_test_case(max_logs, queries)