from rest_framework import serializers
from apps.connections.models import SourceConnectionDtls, DestinationConnectionDtls

class SourceConnectionDtlsSerializer(serializers.ModelSerializer):
    class Meta:
        model=SourceConnectionDtls
        fields=('SrcId','SrcType','SrcNm', 'BigQueryProjectId', 'BigQueryServiceAccountKeyFileLocation')

class DestinationConnectionDtlsSerializer(serializers.ModelSerializer):
    class Meta:
        model=DestinationConnectionDtls
        fields=('DestId','DestType','DestNm', 'DestUname', 'DestPwd')