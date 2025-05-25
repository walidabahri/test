from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add custom claims
        # Determine if user is a manager based on groups or permissions
        # Assuming managers are in a group called 'Manager' and others are workers
        is_manager = user.groups.filter(name='Manager').exists()
        
        # Add user role to token
        token['role'] = 'manager' if is_manager else 'worker'
        
        # Add additional user info if needed
        token['username'] = user.username
        
        return token
    
    def validate(self, attrs):
        # The original validate method returns the access and refresh tokens
        data = super().validate(attrs)
        
        # Add extra responses here
        # Get user role info to return directly in the response
        is_manager = self.user.groups.filter(name='Manager').exists()
        data['user_role'] = 'manager' if is_manager else 'worker'
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
