
import threading


class BufferWriter: 
    
    def __init__(self, file, buffer_size):
        
        if buffer_size <= 0:
            raise ValueError("Buffer Size cannot be less than 0")
        self.buffer_size = buffer_size
        self.file = file
        self.buffer = []
        self.current_size = 0 
        self.lock = threading.Lock()
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()
        return False
            
    def write(self, data, buffer_size): 
        
        if not data:
            return 
        with self.lock:
            if len(data) >= self.buffer_size:
                #write directtly to memory 
                self.file.write(data)
                self._flush__internal()
            self.buffer.append(data)
            self.current_size += len(data)
            
            if self.current_size >= buffer_size:
                self._flush__internal()
        
    
    def flush (self):
        with self.lock:
            self.__flush__internal()
        
    
    def _flush__internal(self):
        if not self.buffer:
            return 

        self.file.write("".join(self.buffer))
        self.buffer = []
        self.current_size = 0
        
        