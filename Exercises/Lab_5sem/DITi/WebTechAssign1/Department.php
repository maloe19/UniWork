<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Department extends Model{
    use HasFactory;
    
    #public $id;
    #public $created_at;
    #public $updated_at;
    #public $name;
    #public $code;
    #public $description;

    protected $id;
    #$table->bigIncrements("id")->unique();
    #$table->foreign("department_id")->references("id")->on("departments"); #tror denne skal i course models
    protected $created_at;
    protected $updated_at;
    protected $name = 'departmentName';
    protected $code = 'department_Code';
    protected $description = ' department description';

    public function course(){
        return $this->hasMany(Course::class);
    }
}