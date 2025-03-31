class Users:
    def __init__(self):
        self.password = 'secret_sauce'
        self.users = [
            'standard_user',
            'locked_out_user',
            'problem_user',
            'performance_glitch_user',
            'error_user',
            'visual_user'
        ]

    def __iter__(self):
        return ((user, self.password) for user in self.users)
