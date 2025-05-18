from models import db, Notification
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notifications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notifications', methods=['POST'])
def send_notif():
    
    data = request.get_json()
    required_fields = ['user_id', 'message', 'type']
    
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    notification_type = data['type'].lower()
    if notification_type not in ['email', 'sms', 'in-app']:
        return jsonify({'error': 'Invalid notification type'}), 400
    
    notification = Notification(
        user_id=data['user_id'],
        message=data['message'],
        type=notification_type,
        status='sent'
    )
    
    db.session.add(notification)
    db.session.commit()
    
    return jsonify({
        'notification_id': notification.id,
        'status': 'sent'
    }), 201

@app.route('/users/<int:user_id>/notifications', methods=['GET'])
def get_notif(user_id):
    
    limit = request.args.get('limit', 10, type=int)
    offset = request.args.get('offset', 0, type=int)
    
    notifications = Notification.query.filter_by(user_id=user_id)\
        .order_by(Notification.created_at.desc())\
        .limit(limit)\
        .offset(offset)\
        .all()
    
    if not notifications:
        return jsonify({'error': 'User not found or no notifications'}), 404
    
    return jsonify({
        'notifications': [{
            'id': n.id,
            'message': n.message,
            'type': n.type,
            'status': n.status,
            'created_at': n.created_at.isoformat()
        } for n in notifications]
    }), 200

if __name__ == '__main__':
    app.run(debug=True)