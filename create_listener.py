import boto3

elb = boto3.client('elbv2')

elb.create_listener(
    LoadBalancerArn='arn:aws:elasticloadbalancing:ap-south-1:475432297908:loadbalancer/net/MyNLB/b77738fdcd51439a',
    Protocol='TCP',
    Port=80,
    DefaultActions=[
        {
            'Type': 'forward',
            'TargetGroupArn': 'arn:aws:elasticloadbalancing:ap-south-1:475432297908:targetgroup/NLBTargetGroup/971d0a7c9e0b88ee'
        }
    ]
)

print("Listener Created")