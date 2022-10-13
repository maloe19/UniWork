<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Course extends Model{
    use HasFactory;
    
    #public $id;
    #public $department_id;
    #public $created_at;
    #public $updated_at;
    #public $name;
    #public $code;
    #public $ects;
    #public $description;

    protected $hidden = [
        'id', 
        'department_id',
        'created_at',
        'updated_at'
    ];

    protected $fillable = [
        'name',
        'code',
        'ects', 
        'description'
    ];

    public function department(){
        return $this->belongsTo(Department::class);
    }
}