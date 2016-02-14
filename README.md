### Quick perf test of dynamodb client libraries

Brendan and the Candi team mentioned they were getting less than 10ms response times from dynamodb with Golang. This 
seemed rather too-good to be true, since we'd been seeing a typical response time around 60 milliseconds with the 
nodeJS aws-sdk. 

So, I decided to do a quick roundup in a few different implmentations to see if I could answer: 

- Were their results accurate? Is the AWS-SDK for node *that* much more terrible that it's roughly 6 times slower?
- if so, Is this becuase dynamic/static typing? 
- Is this simply the different consistency models being defaulted to different options (ie eventual vs strong)? 
- Could this just be a maturity thing/some weird thing I've not thought of? 

### Method:

So:

1. I turned off strong consistency for all implementations (where it was obvious, dunno about amazonica/faraday, I think it defaults here anyway).
2. Did a simple loop for a record, waiting for 1 second between calls so as not to make it an IOPS bound thing
3. Threw the applications into an ec2 instance and executed them
3. Recorded results

### Results: 

![result](https://raw.githubusercontent.com/davidporter-id-au/debugging-node-aws-perf/master/perf.png)

raw results are just a stdout dump in /results/*.log

### Conclusion

1. Yep, NodeJS appears to be performing terribly. 
2. This can't be a dynamic-languages-aren't-fast thing, python's only a couple of milliseconds off golang
3. I still don't know what's going on with node. I'll have to do some flame-graphs or something. 
4. Clojure/JVM seem to take a while to 'warm up', then they perform reasonably well
