'''
Created on Oct 16, 2013

@author: Mark
'''
import time
import mmap
import binascii

class BryCompress:
    
    def compress(self, inputfilepath, outputfilepath):
        #Super slow
        #=======================================================================
        # binaryFile = ""
        # try:
        #     fin = open(inputfilepath, 'r')
        #     bytes = (ord(b) for b in fin.read())
        #     for bit in bytes:
        #         for i in xrange(7, -1, -1):
        #             rawbit = (bit >> i) & 1
        #             binaryFile = binaryFile + str(rawbit)
        # finally:
        #     print "done"
        #     fin.close()
        #     
        # fileInt = int(binaryFile, 2)
        #=======================================================================
        
        #Worked well but I was reading the file at 3KBs
        #=======================================================================
        # fileInt = 0
        # try:
        #     count = 0
        #     startTime = time.time()
        #     fin = open(inputfilepath, 'r')
        #     bytes = (ord(b) for b in fin.read())
        #     for byte in bytes:
        #         fileInt = fileInt << 8
        #         fileInt = fileInt + byte
        #         count = count + 1
        #         secPassed = int(time.time()-startTime)
        #         if(secPassed != 0):
        #             print count/secPassed
        # finally:
        #     fin.close()
        #=======================================================================
        
        
        #=======================================================================
        # fileInt = 0
        # try:
        #     startTime = time.time()
        #     fin = open(inputfilepath, "r+b")
        #     mem = mmap.mmap(fin.fileno(), 0)
        #     byte = mem.read(1)
        #     while (byte != ""):
        #         fileInt = fileInt << 8
        #         fileInt = fileInt + ord(byte)
        #         byte = mem.read(1)
        # finally:
        #     print "Done in: " + int(time.time()-startTime)
        #     fin.close()
        #=======================================================================
            
        fileInt = 0
        s = ""
        try:
            startTime = time.time()
            fin = open(inputfilepath, "r+b")
            s = fin.read()
        finally:
            fin.close()
            print "Done reading file in: " + str(time.time()-startTime)
        
        #Generate int   
        binaryString = ""
        print "Starting to make binary string"
        startTime = time.time()
        for char in s:
            binaryString = binaryString + str(bin(ord(char)))[2:]
        print binaryString
        print "Done making b string in: " + str(time.time()-startTime)
        
        print "Starting to make big int"
        startTime = time.time()
        fileInt = int(binaryString, 2)
        print fileInt
        print "Done making file int in: " + str(time.time()-startTime)
        
        
        halfFileInt = fileInt/4;
        
        for base in xrange(2, 128):
                for power in xrange(2, 128):
                    attempt = fileInt - base**power
                    if (attempt < halfFileInt and attempt > 0 ):
                        print str(base) + " " + str(power)
                        print fileInt
                        print (fileInt - base**power)
                        break;
        print "none found :("
        
    
    def decompress(self, inputfilepath, outputfilepath):
        pass

if __name__ == "__main__":
    bry = BryCompress()

    bry.compress("dic.txt", "bry.bry")

    #bry.decompress("bry.txt", "brydic.txt")