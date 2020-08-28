from aws_cdk import (
    core,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins
)


class CdkCloudfrontOriginStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        cdnOrigin = core.CfnParameter(self, "cdnOrigin", type="String", description="CDN origin hostname")

        cdnDistribution = cloudfront.Distribution(self, "cdnDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                allowed_methods=cloudfront.AllowedMethods.ALLOW_ALL,
                cached_methods=cloudfront.CachedMethods.CACHE_GET_HEAD,
                compress=True,
                forward_query_string=True,
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                origin=origins.HttpOrigin(
                    domain_name=cdnOrigin.value_as_string,
                    protocol_policy=cloudfront.OriginProtocolPolicy.HTTPS_ONLY
                )
            ),
            #certificate="<I wish to push here arn string which is store in variable: config.cdnCertArn variable>"
            #domain_names=['front.' + config.stackName + '.' + config.hostedZone],
            #comment="CDN distribution for front." + config.stackName + '.' + config.hostedZone,
            enable_ipv6 = False,
            #http_version=aws_cloudfront.HttpVersion.HTTP1_1,
            enabled = True
        )