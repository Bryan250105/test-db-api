from flask import request, jsonify, url_for
from app import db
from app.models import PortCodeList, AirportCodeList
from app.main import bp

# Helper function untuk pagination metadata
def get_paginated_list(model, endpoint):
    # 1. Ambil Parameter dari URL
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 20, type=int), 250) # Maksimal 250 data
    
    # 2. Ambil semua kolom model untuk filtering otomatis
    query = model.query
    model_columns = model.__table__.columns.keys()
    
    # 3. Dynamic Filtering (WHERE statement)
    for key, value in request.args.items():
        if key in model_columns:
            # Menggunakan ilike untuk pencarian teks agar tidak case-sensitive
            column_attr = getattr(model, key)
            if isinstance(column_attr.type, db.Text) or isinstance(column_attr.type, db.String):
                query = query.filter(column_attr.ilike(f"%{value}%"))
            else:
                query = query.filter(column_attr == value)

    # 4. Eksekusi Pagination
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)

    args = request.args.to_dict()
    args.pop('page', None)
    args.pop('per_page', None)
    
    # 5. Susun Response JSON
    return jsonify({
        'data': [item.to_dict() for item in pagination.items],
        'meta': {
            'page': pagination.page,
            'per_page': pagination.per_page,
            'total_pages': pagination.pages,
            'total_items': pagination.total,
            'has_next': pagination.has_next,
            'has_prev': pagination.has_prev,
            'next_page': url_for(endpoint, page=pagination.next_num, per_page=per_page, _external=True, **args) if pagination.has_next else None,
            'prev_page': url_for(endpoint, page=pagination.prev_num, per_page=per_page, _external=True, **args) if pagination.has_prev else None,
        }
    })

# --- ROUTES ---

@bp.route('/ports', methods=['GET'])
def get_ports():
    return get_paginated_list(PortCodeList, 'main.get_ports')

@bp.route('/airports', methods=['GET'])
def get_airports():
    return get_paginated_list(AirportCodeList, 'main.get_airports')

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "online", "message": "API is running"}), 200