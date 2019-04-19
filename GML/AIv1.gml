  var Distance;
var Target : Transform;
var lookAtDistance = 25.0;
var chaseRange = 15.0;
var attackRange = 1.5;
var moveSpeed = 5.0;
var Damping = 6.0;

var controller : CharacterController;
var gravity : float = 20.0;
private var MoveDirection : Vector3 = Vector3.zero;

function Update()
{
	Distance = Vector3.Distance(Target.position, transform.position);
	
	if (Distance < lookAtDistance)
	{
		lookAt();
	}
	
	if (Distance > lookAtDistance)
	{
		renderer.material.color = Color.green;
	}
	
	if (Distance < attackRange)
	{
		attack();
	}
	else if (Distance < chaseRange)
	{
		chase();
	}
}

function lookat()
{
	renderer.material.color = Color.yellow;
	var rotation = Quaternion.LookRoatation(Target.position - transform.position);
	transform.rotation = Quaternion.Slerp(transform.rotation, rotationm Time,deltaTime * Damping);
}

function chase ()
{
	renderer.material.color = Color.red;
	
	moveDirection = transform.forward;
	moveDirection *= moveSpeed;
	
	moveDirection.y -= gravity * Time.deltaTime);
	controller.Move(moveDirection * Time.deltaTime);
}

function attack()
{
	Debug.Log("Attack");
}
