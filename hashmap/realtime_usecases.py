from collections import defaultdict

class Usecases:
    
    def __init__(self):
        self.seen_alerts = set()
        self.active_host = set()
        self.request_count = defaultdict(int)
    
    def depulicating_alerts(self, alert_id):
        "# Same alert firing 1000x — only notify once"
        
        if alert_id in self.seen_alerts:
            return 
        self.seen_alerts.add(alert_id)
        #send_notification(alert_id)
        
    
    def unique_active_host(self,host, metric):
        
        self.active_host.add(host) # automatically deuplicates it 
        
        print(len(self.unique_active_host))
        
        
    def log_error(self, service, error):
        """
        Tracking Error Rate Per Service
        
        """
        
        from collections import defaultdict
        
        error_count = defaultdict(int)
        
        error_count[service] += 1
        
        return error_count
    
    
    def metric_aggregation(self, service, value) : 
        
        """
        # Given a stream of metrics, find the top K services by request count
        """   
        
        
        self.request_count[service] += value
        
        # top = sorted(self.request_count, key = self.request_count.get , reverse=True)[:3]
        
        
    def cache_last_known_state():
        
        # Store last heartbeat time per host
        last_seen = {}
        
        def heartbeat(host, timestamp):
            last_seen[host] = timestamp
            
        def is_dead(host, now, threshold=30):
            if host not in last_seen:
                return True
            return (now - last_seen[host]) > threshold
            

        def ingest_span(trace_id, span):
            traces = defaultdict(list)
            traces[trace_id].append(span)   # same pattern as groupAnagrams

        # traces = {
        #   "abc123": [span1, span2, span3],  ← one full request trace
        #   "xyz789": [span4, span5]
        # }
        
        
        
        
    
        
    
        
        