
class SliceableDict(dict):
    def __getitem__(self, key):
        if isinstance(key, slice):
            # Determine the full range of indices from the slice
            start = key.start if key.start is not None else 0
            stop = key.stop if key.stop is not None else max(self.keys(), default=0) + 1
            step = key.step if key.step is not None else 1
            
            # Generate the range of keys based on the slice
            indices = range(start, stop, step)
            
            # Fetch values, defaulting to 0 if the key is missing
            return [self.get(i, 0) for i in indices]
        
        # For single key access, return 0 if the key doesn't exist
        return self.get(key, 0)
