UVICORN_OPTIONS = {
    'access_log': False, #시스템에 log print를 안함,
}

TITLE = 'Console API for Cloudforet'
DESCRIPTION = ''


CONNECTORS = {
    'SpaceConnector': {
        'backend': 'spaceone.core.connector.space_connector.SpaceConnector',
        'endpoints': {
            # 'identity': 'grpc://identity:50051/v1',
            # 'inventory': 'grpc://inventory:50051/v1',
            # 'repository': 'grpc://repository:50051/v1',
            # 'secret': 'grpc://secret:50051/v1',
            # 'plugin': 'grpc://plugin:50051/v1',
            # 'monitoring': 'grpc://monitoring:50051/v1',
            # 'statistics': 'grpc://statistics:50051/v1',
            # 'notification': 'grpc://notification:50051/v1',
            # 'config': 'grpc://config:50051/v1',
            # 'cost_analysis': 'grpc://cost-analysis:50051/v1',
            # 'board': 'grpc://board:50051/v1',
            # 'file_manager': 'grpc://file-manager:50051/v1',
            'dashboard': 'grpc://dashboard:50051/v1',
        }
    },
}
